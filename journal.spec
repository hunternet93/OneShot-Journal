# -*- mode: python -*-

block_cipher = None

a = Analysis(['journal.py'],
             pathex=['.'],
             binaries=[],
             datas=[('images', 'images')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='_______',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='_______')
app = BUNDLE(coll,
             name='_______.app',
             icon=None,
             bundle_identifier="queengooborg.oneshot-game.osx-journal",
             info_plist={
              "CFBundlePackageType": "APPL",
              "CFBundleShortVersionString": "1.0",
              "CFBundleGetInfoString": "You only have one shot.",
              "CFBundleVersion": "1.0",
              "LSApplicationCategoryType": "public.app-category.games",
              "NSHumanReadableCopyright": "Copyright © 2017, OneShot team, all rights reserved.  View CREDITS.txt for more.  Port for macOS copyright © 2017, hunternet93 and Vinyl Darkscratch, MIT License. https://github.com/hunternet93/OneShot-Journal",
              "NSHighResolutionCapable": True
              }
            )
