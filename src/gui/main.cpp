#include "finderwindow.h"
#include "settings.h"
#include <QApplication>
#include <iostream>

int main(int argc, char *argv[])  {

	QApplication a(argc, argv);

	QDir::setCurrent(QCoreApplication::applicationDirPath());

	std::cout << a.applicationFilePath().replace('/','\\').toStdString() << std::endl;

	FinderWindow w;
	Settings::getInstance()->setMainWindow(&w);
    a.setApplicationName("Fetch");

	if (w.isAlreadyRunning()) {
		return 0;
	}

	w.init();
    w.startListening();

	return a.exec();
}
