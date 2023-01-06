#Quadratic function solver
import math

def root_determinants(a,b,c):
    roots_checker= (b**2) -4*(a*c)
    if roots_checker < 0:
        return f"{a}x^2 +{b}x+{c} has Complex Roots"
    elif roots_checker == 0:
        return f"{a}x^2 +{b}x+{c} has Equal Roots"
    elif roots_checker > 0:
        return f"{a}x^2 +{b}x+{c} has Real Roots"
    else:
        return f"Check your varriables passed into your equation well" 

def quadratic_equation_postive(a,b,c):
    roots_resolver=(b**2)-4*(a*c)
    x_numerator=-(b)+math.sqrt(roots_resolver)
    x_denominator=2*a
    x=x_numerator/x_denominator
    return f"For Positive Root  {x} "
    
def quadratic_equation_postive(a,b,c):
    roots_resolver=(b**2)-4*(a*c)
    x_numerator=-(b)-math.sqrt(roots_resolver)
    x_denominator=2*a
    x=x_numerator/x_denominator
    return f"For Negative Root  {x} "
    
    
print("import_dev.py",__name__)
# print(root_determinants(2,3,4))