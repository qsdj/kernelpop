"""
Class for holding kernel windows for vulnerabilities
"""
from src.kernelpop import Kernel

class KernelWindow:
	def __init__(self, distro, confirmation, lowest_major, lowest_minor, lowest_release, highest_major, highest_minor,
		highest_release):
		self.distro = 			distro
		self.confirmation = 	confirmation 	# string, either 'confirmed' or 'potential'
		self.lowest_major = 	lowest_major
		self.lowest_minor = 	lowest_minor
		self.lowest_release = 	lowest_release
		self.highest_major = 	highest_major
		self.highest_minor = 	highest_minor
		self.highest_release = 	highest_release

	def kernel_in_window(self, kernel):
		"""
		Returns True if the given Kernel object is within the kernel window
		:param kernel: Kernel object
		:return: True or False
		"""
		# check for self.distro in kernel.distro so that we can match generics to all kernels of a type:
		# 	i.e. "debian" will be in "debian7" and "debian8" etc...
		if self.distro in kernel.distro and self.lowest_major <= kernel.major_version <= self.highest_major and \
			self.lowest_minor <= kernel.minor_version <= self.highest_minor and self.lowest_release <= kernel.release\
			<= self.highest_release:
			return self.confirmation
		else:
			return "no"