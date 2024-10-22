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
# java_fpath = install_java(jre_dpath, java_version = "11")
# this depends on setup:
java_fpath = os.path.abspath("/media/souto/257-FLASH/dev/python-jdk-test/jre/jdk-11.0.25+9-jre/bin/java")

# test

omtprj_dpath = os.path.abspath("/home/souto/Work/TEST_ara-ZZZ_OMT")
script_fpath = os.path.abspath("/home/souto/.omegat_572_jre11/scripts/project_changed/pisa25trend.groovy")
omegat_translate_command = f"{java_fpath} -jar {omtjar_fpath} {omtprj_dpath} --script={script_fpath} --mode=console-translate"
print(f"Do: {omegat_translate_command=}")
os.system(omegat_translate_command)

# install config
# use script


# two approaches to install JRE: 
# download omegat without jre and then install jre separately
# or ./gradlew linux to create bundle including jre
# the size is similar in both cases

# two cases: 
# input is REPO OR OMT PACKAGE

# two APIs
# - omegat-compile
# - omegat-compile-and-commit

# The latter calls the former? no

# input is either:
# - omt package
# - repo url

# returns:
# - target folder bundle
# - commit hash

# Parameters:
# - script
# - script
# - script


