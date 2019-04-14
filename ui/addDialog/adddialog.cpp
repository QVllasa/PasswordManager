#include "adddialog.h"
#include "ui_adddialog.h"

addDialog::addDialog(QWidget *parent) :
    QWidget(parent),
    ui(new Ui::addDialog)
{
    ui->setupUi(this);
}

addDialog::~addDialog()
{
    delete ui;
}
