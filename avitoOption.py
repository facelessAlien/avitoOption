from mainWindow import main

if __name__ == '__main__':
    main()

# nuitka --mingw64 --follow-imports --standalone --onefile --windows-icon-from-ico="C:\Users\PC\PycharmProjects\AvitoScrapperTest\ico\avito.ico" --output-filename="avitoOption.exe" --windows-disable-console  --enable-plugin=pyside6 .\avitoOption.py