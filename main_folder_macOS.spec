# -*- mode: python -*-

block_cipher = None


a = Analysis(['main_macOS.py'],
             pathex=['/Users/qendrimvllasa/Library/Mobile Documents/com~apple~CloudDocs/Projects/Password Manager'],
             binaries=[('webdriver/macOS/chromedriver', 'webdriver/macOS'),
             ('webdriver/macOS/geckodriver', 'webdriver/macOS')],
             datas=[('/Users/qendrimvllasa/anaconda3/lib/python3.7/site-packages/docx/templates/default.docx', "docx/templates"),('mdsp_password_manager.icns','.')
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
          exclude_binaries=True,
          name='Password Manager',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          runtime_tmpdir=None,
          console=False, icon='mdsp_password_manager.icns' )




