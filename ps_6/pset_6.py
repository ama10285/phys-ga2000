from astropy.io import fits
import matplotlib.pyplot as plt
import numpy as np
hdu_list = fits.open(r'C:\Users\HP-ENVY\Downloads\\specgrid.fits')
logwave = hdu_list['LOGWAVE'].data
flux = hdu_list['FLUX'].data
plt.plot(logwave, flux[0, :])
plt.plot(logwave, flux[1, :])
plt.plot(logwave, flux[2, :])
plt.plot(logwave, flux[3, :])
plt.plot(logwave, flux[4, :])

plt.ylabel('flux [$10^{−17}$ erg s$^{−1}$ cm$^{−2}$ A$^{-1}$]', fontsize = 16)
plt.xlabel('wavelength [$A$]', fontsize = 16)
plt.show()
# find normalization over wavelength for each galaxy
flux_sum = np.sum(flux, axis = 1)
flux_normalized = flux/np.tile(flux_sum, (np.shape(flux)[1], 1)).T

#check that the data is properly "normalized"
plt.plot(np.sum(flux_normalized, axis = 1))
plt.ylim(0,2)
plt.show()

# subtract off mean
means_normalized = np.mean(flux_normalized, axis=1)
flux_normalized_0_mean = flux_normalized-np.tile(means_normalized, (np.shape(flux)[1], 1)).T
plt.plot(logwave, flux_normalized_0_mean[0,:]*(10**4))
plt.ylabel('normalized 0-mean flux', fontsize = 16)
plt.xlabel('wavelength [$A$]', fontsize = 16)
plt.show()



def sorted_eigs(r, return_eigvalues = False):
    """
    Calculate the eigenvectors and eigenvalues of the correlation matrix of r
    -----------------------------------------------------
    """
    corr=r.T@r
    eigs=np.linalg.eig(corr) #calculate eigenvectors and values of original 
    arg=np.argsort(eigs[0])[::-1] #get indices for sorted eigenvalues
    eigvec=eigs[1][:,arg] #sort eigenvectors
    eig = eigs[0][arg] # sort eigenvalues
    if return_eigvalues == True:
        return eig, eigvec
    else:
        return eigvec

r = flux_normalized_0_mean 
r_subset = r[:500, :]

means_normalized = np.mean(flux_normalized, axis=1)
flux_normalized_0_mean = flux_normalized - np.tile(means_normalized, (np.shape(flux)[1], 1)).T

eigvals,eigvecs = sorted_eigs(r_subset, return_eigvalues= True)


# the covariance matrix
C = np.cov(flux_normalized_0_mean.T)
eigvec = sorted_eigs(flux_normalized_0_mean)
num_eigenvectors_to_plot = 5
for i in range(num_eigenvectors_to_plot):
    plt.plot(logwave, eigvec[:, i], label=f'Eigenvector {i+1}')

plt.xlabel('Wavelength [$\AA$]', fontsize=16)
plt.ylabel('Amplitude', fontsize=16)
plt.title('First Five Eigenvectors from PCA', fontsize=18)
plt.legend()
plt.show()
    
    
    
U, S, Vh = np.linalg.svd(r_subset, full_matrices=True)
print("condition number R =", np.max(S)/np.min(S))
eigvecs_svd = Vh.T
eigvals_svd = S**2
svd_sort = np.argsort(eigvals_svd)[::-1]
eigvecs_svd = eigvecs_svd[:,svd_sort]
eigvals_svd = eigvals_svd[svd_sort]


[plt.plot(eigvecs_svd[:,i], eigvecs[:,i], 'o')for i in range(100)]
plt.plot(np.linspace(-0.2, 0.2), np.linspace(-0.2, 0.2))
plt.xlabel('SVD eigenvalues', fontsize = 16)
plt.ylabel('Eig eigenvalues', fontsize = 16)
plt.show()
plt.plot(eigvals_svd, eigvals[:500], 'o')
plt.xlabel('SVD eigenvalues', fontsize = 16)
plt.ylabel('Eig eigenvalues', fontsize = 16)
plt.show()

def PCA(l, r, project = True):
    """
    Perform PCA dimensionality reduction
    --------------------------------------------------------------------------------------
    """
    eigvector = sorted_eigs(r)
    eigvec=eigvector[:,:l] #sort eigenvectors, only keep l
    reduced_wavelength_data= np.dot(eigvec.T,r.T) #np.dot(eigvec.T, np.dot(eigvec,r.T))
    if project == False:
        return reduced_wavelength_data.T # get the reduced wavelength weights
    else: 
        return np.dot(eigvec, reduced_wavelength_data).T # multiply eigenvectors by 
                                                        # weights to get approximate spectrum
        
plt.plot(logwave, PCA(1,r_subset)[1,:], label = 'l = 5')
plt.plot(logwave, r_subset[1,:], label = 'original data')

plt.ylabel('normalized 0-mean flux', fontsize = 16)
plt.xlabel('wavelength [$A$]', fontsize = 16)
plt.legend()
plt.show()


# Assuming you have the eigenvectors stored in eigvec_svd
# Calculate coefficients c0, c1, c2 for the first 5 spectra
coefficients = np.dot(flux_normalized_0_mean[:, :5], eigvecs_svd[:, :5].T)

# Plot c0 vs c1 and c0 vs c2
plt.scatter(coefficients[:, 0], coefficients[:, 1], label='c0 vs c1')
plt.xlabel('c0', fontsize=16)
plt.ylabel('c1', fontsize=16)
plt.legend()
plt.show()

plt.scatter(coefficients[:, 0], coefficients[:, 2], label='c0 vs c2')
plt.xlabel('c0', fontsize=16)
plt.ylabel('c2', fontsize=16)
plt.legend()
plt.show()

# Perform PCA with Nc = 20
approx_spectra_20 = PCA(20, r)

# Calculate squared fractional residuals for Nc = 20
squared_residuals_20 = np.sum((flux_normalized_0_mean - approx_spectra_20)**2) / np.sum(flux_normalized_0_mean**2)

# Print the fractional error for Nc = 20
print(f'Fractional error for Nc = 20: {squared_residuals_20:.6f}')