from setuptools import setup, find_packages
import os, sys, glob, fnmatch

setup(name="asciisciit",
      version=0.1,
      description="asciisciit is a Python toolbox for displaying and converting images, movies, and camera feeds into ascii.",
      long_description="""asciisciit is a Python toolbox for displaying and converting images, movies, gifs, and webcam feeds into ASCII.  It uses OpenCV, Numpy, and PIL for image processing, and is tested on windows and linux.""",
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'Intended Audience :: Religion',
          'Intended Audience :: End Users/Desktop',
          'License :: OSI Approved :: MIT License',
          'Operating System :: Windows',
          'Operating System :: POSIX :: Linux'
          'Programming Language :: Python',
          'Topic :: Multimedia :: Graphics :: Capture :: Digital Camera',
          'Topic :: Multimedia :: Graphics :: Graphics Conversion',
          'Topic :: Multimedia :: Video :: Capture',
          'Topic :: Multimedia :: Video :: Display',
          'Topic :: Graphics :: Viewers',
          'Topic :: Software Development :: Libraries :: Python Modules'],
      keywords='ascii, opencv, PIL, terminal',
      author='Derric Williams',
      author_email='derricw@gmail.com',
      url='https://github.com/derricw/asciisciit',
      license='MIT',
      packages=find_packages(),
      zip_safe=True,
      requires=['cv2', 'cv', 'numpy', 'pil'],
      package_data = {"":["res/*.ttf"]},
      entry_points = {'console_scripts': ['asciit = asciisciit.asciit:main',],},
      )

