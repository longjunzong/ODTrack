class EnvironmentSettings:
    def __init__(self):
        self.workspace_dir = '/home/host/Steam/ODTrack'    # Base directory for saving network checkpoints.
        self.tensorboard_dir = '/home/host/Steam/ODTrack/tensorboard'    # Directory for tensorboard files.
        self.pretrained_networks = '/home/host/Steam/ODTrack/pretrained_networks'
        self.lasot_dir = '/home/host/Devdata/TrackingDataset/track_train_dataset/LaSOT'
        self.got10k_dir = '/home/host/Devdata/TrackingDataset/track_train_dataset/GOT-10k/train'
        self.got10k_val_dir = '/home/host/Steam/ODTrack/data/got10k/val'
        self.lasot_lmdb_dir = '/home/host/Steam/ODTrack/data/lasot_lmdb'
        self.got10k_lmdb_dir = '/home/host/Steam/ODTrack/data/got10k_lmdb'
        self.trackingnet_dir = '/home/host/data/TrackingNet'
        self.trackingnet_lmdb_dir = '/home/host/Steam/ODTrack/data/trackingnet_lmdb'
        self.coco_dir = '/home/host/Devdata/TrackingDataset/track_train_dataset/COCO'
        self.coco_lmdb_dir = '/home/host/Steam/ODTrack/data/coco_lmdb'
        self.lvis_dir = ''
        self.sbd_dir = ''
        self.imagenet_dir = '/home/host/Steam/ODTrack/data/vid'
        self.imagenet_lmdb_dir = '/home/host/Steam/ODTrack/data/vid_lmdb'
        self.imagenetdet_dir = ''
        self.ecssd_dir = ''
        self.hkuis_dir = ''
        self.msra10k_dir = ''
