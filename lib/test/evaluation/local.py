from lib.test.evaluation.environment import EnvSettings

def local_env_settings():
    settings = EnvSettings()

    # Set your local paths here.

    settings.davis_dir = ''
    settings.got10k_lmdb_path = '/home/host/Steam/ODTrack/data/got10k_lmdb'
    settings.got10k_path = '/home/host/Steam/ODTrack/data/got10k'
    settings.got_packed_results_path = ''
    settings.got_reports_path = ''
    settings.itb_path = '/home/host/Steam/ODTrack/data/itb'
    settings.lasot_extension_subset_path = '/home/host/Steam/ODTrack/data/lasot_extension_subset'
    settings.lasot_lmdb_path = '/home/host/Steam/ODTrack/data/lasot_lmdb'
    settings.lasot_path = '/home/host/Steam/ODTrack/data/lasot'
    settings.network_path = '/home/host/Steam/ODTrack/output/test/networks'    # Where tracking networks are stored.
    settings.nfs_path = '/home/host/Steam/ODTrack/data/nfs'
    settings.otb_path = '/home/host/Steam/ODTrack/data/otb'
    settings.prj_dir = '/home/host/Steam/ODTrack'
    settings.result_plot_path = '/home/host/Steam/ODTrack/output/test/result_plots'
    settings.results_path = '/home/host/Steam/ODTrack/output/test/tracking_results'    # Where to store tracking results
    settings.save_dir = '/home/host/Steam/ODTrack/output'
    settings.segmentation_path = '/home/host/Steam/ODTrack/output/test/segmentation_results'
    settings.tc128_path = '/home/host/Steam/ODTrack/data/TC128'
    settings.tn_packed_results_path = ''
    settings.tnl2k_path = '/home/host/Steam/ODTrack/data/tnl2k'
    settings.tpl_path = ''
    settings.trackingnet_path = '/home/host/Steam/ODTrack/data/trackingnet'
    settings.uav_path = '/home/host/Steam/ODTrack/data/uav'
    settings.vot18_path = '/home/host/Steam/ODTrack/data/vot2018'
    settings.vot22_path = '/home/host/Steam/ODTrack/data/vot2022'
    settings.vot_path = '/home/host/Steam/ODTrack/data/VOT2019'
    settings.youtubevos_dir = ''

    return settings

