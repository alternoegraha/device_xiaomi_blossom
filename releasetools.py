#
# Copyright (C) 2023 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

import common
import re

def FullOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def IncrementalOTA_InstallEnd(info):
  OTA_InstallEnd(info)
  return

def AddImage(info, basename, dest):
  name = basename
  data = info.input_zip.read("IMAGES/" + basename)
  common.ZipWriteStr(info.output_zip, name, data)
  info.script.AppendExtra('package_extract_file("%s", "%s");' % (name, dest))

def OTA_InstallEnd(info):
  info.script.Print("Patching firmware images...")
  AddImage(info, "vbmeta.img", "/dev/block/platform/bootdevice/by-name/vbmeta")
  AddImage(info, "vbmeta_system.img", "/dev/block/platform/bootdevice/by-name/vbmeta_system")
  AddImage(info, "vbmeta_vendor.img", "/dev/block/platform/bootdevice/by-name/vbmeta_vendor")
  AddImage(info, "dtbo.img", "/dev/block/platform/bootdevice/by-name/dtbo")
  info.script.Print("Thanks for using the ROM!")
  info.script.Print("Sushrut1101 for his original 64bit work")
  info.script.Print("Sad_Yurri for his original opensource tree")
  info.script.Print("snnbyyds for building the ROM and small")
  info.script.Print("contributions")
  return
