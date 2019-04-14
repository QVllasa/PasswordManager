#include "adddialog.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);
    addDialog w;
    w.show();

    return a.exec();
}
