
# Preprocessing Steps

1. Skull Stripping (Only for anatomical/structural data)
2. Motion correction
3. Slice Timing Correction
4. Smoothing
5. Registration and Normalization

Then, you need to segment the images, use segmentation feature in SPM12. After
the brain is segmented into three different types of tissue, Grey Matter, White
Matter and CSF, you need to create a common mask for white matter and grey
matter. This should conclude preprocessing in its strict terms. Before
calculating FC, we need to then remove covariates.
