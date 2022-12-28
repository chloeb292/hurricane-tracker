import csv
import turtle
import os
import glob


def graphical_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return t, wn, map_bg_img


def track_storm(filename):
    """Animates the path of the storm.
    """

    (t, wn, map_bg_img) = graphical_setup()
    with open(filename, mode ='r')as file:
        t.penup()
        t.hideturtle()
        # reading the CSV file
        csvFile = csv.reader(file)
        # displaying the contents of the CSV file
        line1 = 1
        for lines in csvFile:
            if(line1):
                line1 = 0
                continue
            else:
                wind_strength = int(lines[4])

                if wind_strength<74 : # not hurricane
                    t.color("white")
                    t.width(1)
                    t.write("")
                elif(wind_strength<96) : # cat 1
                    t.color("blue")
                    t.width(2)
                    t.write("1")
                elif(wind_strength<111): # cat 2
                    t.color("green")
                    t.width(3)
                    t.write("2")
                elif(wind_strength<130): # cat 3
                    t.color("yellow")
                    t.width(7)
                    t.write("3")
                elif(wind_strength<157): # cat 4
                    t.color("orange")
                    t.width(11)
                    t.write("4")
                else:
                    t.color("red")
                    t.width(15)
                    t.write("5")
                
                t.goto(float(lines[3]),float(lines[2]))
                t.pendown()
                t.showturtle()
    



    # your code to animate storm here

    # your code above this
    # without the final call to wn.exitonclick() in main,
    # the background image will not be displayed
    # also need to return map_bg_img so that it is not garbage collected
    return t, wn, map_bg_img


def main():
    # wn.exitonclick()
    have_hurricane = 0
    hurricane_name = "data/" + input("Enter name of storm: ") + ".csv"
    for file in glob.glob("data/*.csv"):
        if file == hurricane_name:
            have_hurricane = 1

    if(have_hurricane):
        t, wn, map_bg_img = track_storm(file)
    else:
        print("Storm not found")


    wn.exitonclick()


main()
