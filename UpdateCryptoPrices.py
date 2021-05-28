#This file should go into 
#For Windows,
#	%APPDATA%\LibreOffice\4\user\Scripts\python.
#For Linux and macOS,
#	$HOME/.config/libreoffice/4/user/Scripts/python.


def UpdateCryptoCurrency(strCurrency, account):
    from lxml import etree
    from datetime import datetime

    desktop = XSCRIPTCONTEXT.getDesktop()
    model = desktop.getCurrentComponent()
    sheet = model.CurrentController.ActiveSheet

    #do a loop that search for the last empty string in column 1
    nCurPosY = 0
    while True:
        cell = sheet.getCellByPosition(1, nCurPosY)
        strValue = cell.getString()

        if strValue == "":
            break

        nCurPosY += 1

    cellToWrite = sheet.getCellByPosition(1, nCurPosY)

    #Get the date data from rowX, Column[0]
    strDate = sheet.getCellByPosition(0, nCurPosY).getString()

    #Open KMyMoneyFile, execute XPath Query and find the proper date
    with open("/home/alainpetit/Documents/Alain Petit/Others/finances.xml") as in_file:
        objDOM = etree.parse(in_file.buffer)

        for res_price_pair in objDOM.xpath("//*[@to='CAD' and @from='"+strCurrency+"']"):

            # Find the latest price quote (in format 1234 / 1000 to give 1.234, kmymoney weird way of manipulating
            # floating points)
            for price in list(res_price_pair):
                strDateKMM = price.get("date")
                strQuoteKMM = price.get("price")
                dataQuoteKMM = strQuoteKMM.split('/')
                leftValue = dataQuoteKMM[0]
                rightValue = dataQuoteKMM[1]
                lastValue = int(leftValue) / int(rightValue)

                if(strDateKMM == strDate):
                    cellToWrite.setValue(lastValue)


                    for transaction in objDOM.xpath("//*[@commodity='"+strCurrency+"' and @postdate='"+strDate+"']"):
                        for splits in list(transaction):
                            for split in list(splits):
                                strAccountKMM = split.get("account")
                                strShareKMM = split.get("shares")

                                if strAccountKMM == account:
                                    dataShareKMM = strShareKMM.split('/')
                                    leftValue = dataShareKMM[0]
                                    rightValue = dataShareKMM[1]
                                    lastValue = int(leftValue) / int(rightValue)
                                    sheet.getCellByPosition(3, nCurPosY).setValue(lastValue)

                    nCurPosY += 1
                    strDate = sheet.getCellByPosition(0, nCurPosY).getString()
                    cellToWrite = sheet.getCellByPosition(1, nCurPosY)


def UpdateCEL(*args):
    UpdateCryptoCurrency("CEL", "A000438")


def UpdateHNT(*args):
    UpdateCryptoCurrency("HNT", "A000455")


def UpdateXYO(*args):
    UpdateCryptoCurrency("XYO", "A000461")

