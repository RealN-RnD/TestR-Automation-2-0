version = "AutomateG1.7"
curScr = Screen(0)
popat(curScr)

aut = "1.14.0.60"
winVariable = ""
macVariable = "Mac OS X 10.10.5" + Key.ENTER + "MacBook Pro (Retina 13-inch Late 2013)" + Key.ENTER + "Model A1502"

isWindows = popAsk("Are you testing on Windows?", version)

while True:
    curScr.click("1470125507873.png")
    popup("Press OK when you have finished testing", version)
    curScr.click("1470125519799.png")
    wait(1)
    if not isWindows:
        curScr.click("1470046377455.png")   
        curScr.paste(macVariable)
    else:
        curScr.click("1470046377455.png")
        curScr.paste(winVariable)
    curScr.click("1470046406673.png")
    curScr.click("1470223593900.png")
    
    curScr.paste(aut)
    curScr.click("1470046187921.png")
    if not isWindows:
        curScr.type("Mac OS X 10.10")
    else:
        curScr.type("Windows 7 64")
    answer = popAsk("Did the test pass?", version)
    if not answer:
        defect = curScr.input("Please enter defect code")
        curScr.click("1470210216668.png")
        curScr.paste(defect)
        popup("Select test steps that failed and change Status", version)
    curScr.click(Pattern("1470644657529.png").similar(0.97))
    wait(1)
    curScr.click("1470126608431.png")
    doWeContinue = popAsk("Another test?", version)
    if not doWeContinue:
        popup("You're Winner", version)
        exit(1)