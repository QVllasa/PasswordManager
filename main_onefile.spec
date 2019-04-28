# -*- mode: python -*-

block_cipher = None


a = Analysis(['main.py'],
             pathex=['/Users/qendrimvllasa/Library/Mobile Documents/com~apple~CloudDocs/Projects/Password Manager'],
             binaries=[('webdriver/windows/chromedriver', 'windows/macOS'),
             ('webdriver/windows/geckodriver', 'webdriver/windows')],
             datas=[('/Users/qendrimvllasa/anaconda3/lib/python3.7/site-packages/docx/templates/default.docx', "docx/templates"),
             ],
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
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='main',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=True )
app = BUNDLE(exe,
             name='main.app',
             icon="mdsp_password_manager.ico",
             bundle_identifier=None)


