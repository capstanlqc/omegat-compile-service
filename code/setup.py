import os
import zipfile
import jdk
from jdk.enums import OperatingSystem, Architecture
import urllib.request
from os.path import dirname, abspath
from git import Repo

code_dir = dirname(abspath(__file__))
app_root = dirname(code_dir)
jre_dpath = os.path.join(app_root, "jre")
# os.makedirs(jre_dpath, mode = 0o777, exist_ok=True)
dist_dir = os.path.join(app_root, "dist")
os.makedirs(dist_dir, mode = 0o777, exist_ok=True)
omtjar_fpath = os.path.join(dist_dir, "OmegaT_5.7.3_Without_JRE", "OmegaT.jar")
config_dpath = os.path.join(dist_dir, "config")


def find_java(directory, target):
    for root, dirs, files in os.walk(directory):
        if target in files:
            # Return the full path to the found file
            return os.path.join(root, target)
    return None


def install_omegat(omtjar_fpath):
    # check if it has not been installed already
    if not os.path.isfile(omtjar_fpath):
        # fetch package
        omtzip_fpath = os.path.join(dist_dir, "OmegaT_5.7.3_Without_JRE.zip")
        urllib.request.urlretrieve("https://cat.capstan.be/OmegaT/exe/5.7.3/OmegaT_5.7.3_Without_JRE.zip", omtzip_fpath)
        # unzip package
        with zipfile.ZipFile(omtzip_fpath, 'r') as zip_ref:
            zip_ref.extractall(dist_dir)

        if os.path.isfile(omtjar_fpath):
            os.remove(omtzip_fpath)
            return True
    else:
        print("OmegaT is already installed")


def install_java(jre_dpath, java_version):
    java_fpath = find_java(jre_dpath, "java")
    if java_fpath is None:
        # jdk.install(java_version, jre=True) # , vendor='Adoptium')
        print(f"JRE is not installed, proceed to install it in {jre_dpath}")
        jdk.install(java_version, jre=True, path=os.path.join(app_root, "jre"))
    
    return find_java(jre_dpath, "java")
  

def clone_repo(repo_url, clone_dir):
    try:
        Repo.clone_from(repo_url, clone_dir)
        print(f"Repository cloned into {clone_dir}")
    except Exception as e:
        print(f"Error during cloning: {e}")


def configure_omegat(config_dpath):
    repo_url = "https://github.com/capstanlqc/omegat-user-config-dev572.git"

    if os.path.isdir(config_dpath) and os.listdir(config_dpath):
       print("OmegaT is already configured")
       return
    
    clone_repo(repo_url, config_dpath)


# check if ~/.jre/jdk-11.0.24+8-jre is found, if not, install :
# jdk.install('11', jre=True) # , vendor='Adoptium')
# Platform dependent install of Java JRE 11 into $HOME/.jre/<VERSION>
# installed in:
# $HOME/.jre/jdk-11.0.24+8-jre/bin/java -version
# java_fpath = "$HOME/.jre/jdk-11.0.25+9-jre/bin/java"

java_fpath = install_java(jre_dpath, java_version = "11")
install_omegat(omtjar_fpath)
configure_omegat(config_dpath)

print(f"{java_fpath=}")


# download_url = jdk.get_download_url(version='11', jre=True)
# print(f"{download_url=}")
# download_file = jdk.download(download_url, version='11')
# print(f"{download_file=}")
# # system checks
# print(jdk.OS)
# print(jdk.ARCH)
# download_file = jdk.download(version='11', operating_system=OperatingSystem.LINUX, arch=Architecture.X64, vendor='Adoptium')
# print(f"{download_file=}") # /tmp/OpenJDK11U-jdk_x64_linux_hotspot_11.0.24_8.tar.gz

# omt_dir = "omt"
# os.makedirs(omt_dir, mode = 0o777, exist_ok=True)
# omtjar_fpath = "/run/media/souto/257-FLASH/dev/python-jdk-test/omt/OmegaT.jar" 
# omtjar_fpath = "/opt/omegat/OmegaT_5.7.2/OmegaT.jar"
# omtjar_fpath = "/run/media/souto/257-FLASH/dev/python-jdk-test/dist/OmegaT_5.7.3_Without_JRE/OmegaT.jar"
# os.path.join(omt_dir, "OmegaT.jar") # 
# print(omtjar_fpath)

