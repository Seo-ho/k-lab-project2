from configs.common_settings import *
model = dict(
    type = 'm2det',
    input_size = 320,
    init_net = True,
    pretrained = 'None', # res series, directly load the pretrained weights when defining them
    m2det_config = dict(
        backbone = 'resnet101',
        net_family = 'res', # vgg includes ['vgg16','vgg19'], res includes ['resnetxxx','resnextxxx']
        base_out = [2,4], # [22,34] for vgg, [2,4] or [3,4] for res families
        planes = 256,
        num_levels = 8,
        num_scales = 6,
        sfam = True,
        smooth = True,
        class_names=['trash','person','bird','cat','cow','dog','horse','sheep',
                    'aeroplane','bicycle','boat','bus','car','motorbike','train',
                    'bottle','chair','dining table','potted plant','sofa',' tv/monitor'],  # class names should be specified
                    
        num_classes=81, # this value is invalid if a class name is specified.
    ),
    rgb_means = (104, 117, 123),
    p = 0.6,
    anchor_config = dict(
        step_pattern = [8, 16, 32, 64, 107, 320],
        size_pattern = [0.08, 0.15, 0.33, 0.51, 0.69, 0.87, 1.05],
        ),
    save_eposhs = 10,
    weights_save = 'weights/'
    )

train_cfg = dict(
    warmup = 5,
    lr = [0.004, 0.002, 0.0004, 0.00004, 0.000004],
    gamma = 0.1,
    end_lr = 1e-6,
    step_lr = dict(
        COCO = [90, 110, 130, 150, 160],
        VOC = [100, 150, 200, 250, 300], # unsolve
        ),
    print_epochs = 10,
    )

test_cfg = dict(
    topk = 0,
    iou = 0.45,
    soft_nms = False,
    score_threshold = 0.7, #0.1 -> 0.5
    keep_per_class = 50,
    save_folder = 'eval'
    )

loss = dict(overlap_thresh = 0.5,
            prior_for_matching = True,
            bkg_label = 0,
            neg_mining = True,
            neg_pos = 3,
            neg_overlap = 0.5,
            encode_target = False)

optimizer = dict(type='SGD', momentum=0.9, weight_decay=0.0005)

