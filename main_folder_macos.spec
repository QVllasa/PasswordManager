# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/qendrimvllasa/Library/Mobile Documents/com~apple~CloudDocs/Projects/Password Manager'],
             binaries=[],
             datas=[('data/accountLists.txt', 'data'),('/Users/qendrimvllasa/anaconda3/lib/python3.7/site-packages/docx/templates/default.docx', "docx/templates"),
             ('webdriver/macOS/chromedriver', 'webdriver/macOS'), ('webdriver/macOS/geckodriver', 'webdriver/macOS')],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=False, icon='mdsp_password_manager.icns' )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='main')

app = BUNDLE(exe,
             name='main.app',
             icon="mdsp_password_manager.icns",
             bundle_identifier=None)
