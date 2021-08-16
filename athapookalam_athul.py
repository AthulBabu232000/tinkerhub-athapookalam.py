from joy import *
inner_c = circle(r = 30)
outer_c = circle(r = 80, fill = "#8227d8")
p1 = point(x = -77, y = -22.67)
p2 = point(x = -77, y = 22.67)
p3 = point(x = 0, y = 0)
tri = polygon([p1, p2, p3], fill = "#e91651")
circle_in_large_c = circle(x=10, y=0, r=5) | repeat(18, rotate(angle=20))
small_c = circle(x = -22, y = 0, r = 11, fill = "purple")
large_c = circle(x = -80, y = 0, r = 20, fill = "#ef52c8")
cin = circle(x= 4, y=0, r=4, stroke = "#fff") | repeat(18, rotate(angle=20)) | translate(-80)
large_c =  large_c + cin
tri =  tri + small_c + large_c  
final_tri = tri | repeat(6, rotate(60))
outer_most_circle = circle(r = 100, fill = "green")
circle_flower = circle(r = 90, x = 70, fill = "blue")
elip = ellipse(x = -40, y = 0, w = 80, h = 23, fill = "yellow") | rotate(30)
elip_final = elip | repeat(6, rotate(60))
inner_elip = ellipse(x = -42, y = 0, w = 60, h = 15, fill = "orange") | rotate(30)
inner_elip_final = inner_elip | repeat(6, rotate(60))
elip_circle = circle(r = 5, fill = "orange")
elip_final = elip_final + inner_elip_final+ elip_circle
inner_group = inner_c + outer_c + elip_final + final_tri
sqp1 = point(x = -90, y = 90)
sqp2 = point(x = -90, y = -90)
sqp3 = point(x = 90, y = -90)
sqp4 = point(x = 90, y = 90)
square = polygon([sqp1, sqp2, sqp3, sqp4], fill = "orange")
final_square = square | repeat(6, rotate(60))
c_outermost = circle(r = 127, fill = "red")
show( c_outermost, final_square, outer_most_circle, inner_group)


