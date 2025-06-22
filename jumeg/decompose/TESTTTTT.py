import os

import mne
from mne.preprocessing import ICA, corrmap, create_ecg_epochs, create_eog_epochs


path_data = 'C:/Users/paula/OneDrive/Escritorio/FourierICA/jumeg/jumeg/data/'
raw_fname = path_data + 'sub-CTR001_ses-V0_task-CE_desc-wavelet_eeg.fif'
#sample_data_folder = mne.datasets.sample.data_path()
sample_data_raw_file = os.path.join(
    raw_fname, "MEG", "sample", "sample_audvis_filt-0-40_raw.fif"
)
raw = mne.io.read_raw_fif(raw_fname, preload=True)

# Here we'll crop to 60 seconds and drop gradiometer channels for speed
raw.crop(tmax=60.0).pick(picks=["mag", "eeg", "stim", "eog"])
raw.load_data()