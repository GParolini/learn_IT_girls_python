my_name = 'Zed A. Shaw'
my_age = 35 #not a lie
my_height = 74.0 #inches
my_weight = 180.0 #lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight)

print "--------"
#drill 1
name = 'Zed A. Shaw'
age = 35
height = 74.0 #inches
weight = 180.0 #lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

#this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "--------"
#drill 2
fruit = 'banana'

print "I like %r no matter what other people say." % fruit
print "I like %s no matter what other people say." % fruit

print "--------"
#drill 3
height_cm = round (height * 2.54)
weight_kilos = round (weight * 0.45359237)

print "Let's talk about %s." % name
print "He's %d cm tall." % height_cm
print "He's %d kilos heavy." % weight_kilos
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

print "If I add %d, %d, and %d I get %d." % (age, height_cm, weight_kilos, age + height_cm + weight_kilos)
