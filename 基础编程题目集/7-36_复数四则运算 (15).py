class Complex(object):
    def __init__(self, real, image):
        self.real = real
        self.image = image
    
    def __add__(self, other):
        r = self.real + other.real
        i = self.image + other.image
        return Complex(r, i)
    
    def __sub__(self, other):
        r = self.real - other.real
        i = self.image - other.image
        return Complex(r, i)

    def __mul__(self, other):
        r = self.real*other.real - self.image*other.image
        i = self.real*other.image + other.real*self.image
        return Complex(r, i)

    def __div__(self, other):
        di = (other.real**2 + other.image**2)
        r = (self.real*other.real + self.image*other.image) / di
        i = (self.image*other.real - self.real*other.image) / di
        return Complex(r, i)
    
    def __str__(self):
        r, i = self.real, self.image
        if -0.05 <= self.image <= 0.05:
            s = '%.1f' % self.real
        elif -0.05 <- self.real <= 0.05:
            s = '%.1fi' % self.image
        elif self.image < 0:
            s = '%.1f%.1fi' % (self.real, self.image)
        else:
            s = '%.1f+%.1fi' % (self.real, self.image)
        return s

    def Expression(self):
        if self.image < 0:
            return '%.1f%.1fi' % (self.real, self.image)
        else:
            return '%.1f+%.1fi' % (self.real, self.image)


a1, b1, a2, b2 = map(float, raw_input().split())
a, b = Complex(a1, b1), Complex(a2, b2)
print '(%s) + (%s) = %s' % (a.Expression(), b.Expression(), a+b)
print '(%s) - (%s) = %s' % (a.Expression(), b.Expression(), a-b)
print '(%s) * (%s) = %s' % (a.Expression(), b.Expression(), a*b)
print '(%s) / (%s) = %s' % (a.Expression(), b.Expression(), a/b)