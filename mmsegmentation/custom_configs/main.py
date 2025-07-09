# Associates a loss to its class and name
losses_mappings = {
    "skil_dice": ("SkilLossDice", "loss_skill_dice"),
    "skil_product": ("SkilLossProduct", "loss_skill_product"),
    "dice": ("DiceLoss", "loss_dice"),
    "cross_entropy": ("CrossEntropyLoss", "loss_ce"),
    "cl_dice": ("ClDiceLoss", "loss_cl_dice"),
}

# Associates a model name to its default weights
default_checkpoint = {
    "vit_vit-b16_mln_upernet_cracks": "https://download.openmmlab.com/mmsegmentation/v0.5/vit/upernet_vit-b16_mln_512x512_160k_ade20k/upernet_vit-b16_mln_512x512_160k_ade20k_20210624_130547-852fa768.pth",
    "vit_vit-b16_mln_upernet_vessels": "https://download.openmmlab.com/mmsegmentation/v0.5/vit/upernet_vit-b16_mln_512x512_160k_ade20k/upernet_vit-b16_mln_512x512_160k_ade20k_20210624_130547-852fa768.pth",
}

# Associates a dataset name to its config file
datasets_mappings = {
    "cracks_combined": "custom_configs.datasets.cracks_combined",
    "vessels_combined": "custom_configs.datasets.vessels_combined",
    "vessels_combined_degraded": "custom_configs.datasets.vessels_combined_degraded",
    "vessels_combined_cropped": "custom_configs.datasets.vessels_combined_degraded_cropped",
    "vessels_combined_shifted": "custom_configs.datasets.vessels_combined_degraded_shifted",
    "vessels_combined_width": "custom_configs.datasets.vessels_combined_degraded_width",
}

# Associates a learning rate schedule name to its config file
schedules_mappings = {
    "aggressive": "custom_configs.schedules.aggressive",
    "40k": "custom_configs.schedules.40k",
}
