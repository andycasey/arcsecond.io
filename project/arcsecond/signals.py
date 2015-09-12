
def process_upon_user_signed_up(sender, **kwargs):
    print 'User signed up', sender, kwargs

def process_upon_user_logged_in(sender, **kwargs):
    print "User logged in", sender, kwargs
