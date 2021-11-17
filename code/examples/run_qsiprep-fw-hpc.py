import flywheel
import datetime

fw = flywheel.Client() #get flywheel Client

qsiprep = fw.lookup('gears/qsiprep-fw-hpc') #find gear of interest
project = fw.projects.find_first("label=gear_testing") #find Flywheel project of interest

now = datetime.datetime.now().strftime("%Y-%m-%d_%H:%M") #define current data/time variable, to be used in labels
analysis_label = 'exampleanalysis_{}_{}_{}'.format(qsiprep.gear.name,qsiprep.gear.version, now) #define a descriptive analysis label

#example config params for qsiprep gear
config = {
            "hmc_model": "eddy",
            "use_syn_sdc": False,
            'b0_threshold': 100,
            'save_outputs': True,
            'dwi_denoise_window': 5,
            'do_reconall': False,
            'b0_to_t1w_transform': 'Rigid',
            'combine_all_dwis': False,
            'intramodal_template_iters': 0,
            'force_spatial_normalization': True,
            'shoreline_iters': 0,
            'output_resolution': 1.5,
            'output_space': 'T1w',
            'sloppy': True,
            'unringing_method': 'mrdegibbs'
        }

inputs = {
    "freesurfer_license": project.files[2],
}

sessions_to_run = []
#Identify sessions to run based on specific session features (here, using acquisition label)
for session in project.sessions():
    desired_session = 'acq-64dir_dwi' in [acq.label for acq in session.acquisitions()]
    if desired_session:
        sessions_to_run.append(session)

analysis_ids = []
fails = []
#Launch gear on identified sessions
for ses in sessions_to_run:
    try:
        _id = qsiprep.run(analysis_label=analysis_label,
                          config=config, inputs=inputs, destination=ses)
        analysis_ids.append(_id)
    except Exception as e:
        print(e)
        fails.append(ses)

#Write analysis IDs and failed sessions to files
with open('{}_{}_{}_analysisIDS.txt'.format(qsiprep.gear.name,qsiprep.gear.version,now), 'w') as f: 
    for id in analysis_ids:
        f.write("%s\n" % id)

with open('{}_{}_{}_failSES.txt'.format(qsiprep.gear.name,qsiprep.gear.version,now), 'w') as a:
    for ses in fails:
        a.write("%s\n" % ses) 
