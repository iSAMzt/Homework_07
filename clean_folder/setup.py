from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='Cleaner3000. Clean Folder',
      author='Oleksii Surskov',
      author_email='alexeysurskov@gmail.com',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': [
          'clean-folder = clean_folder.clean:start']}
      )
