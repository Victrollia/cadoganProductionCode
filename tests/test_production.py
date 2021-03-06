import main

milk = main.Products('milk', 2.99, 'WIC Eligible')
tee = main.Products('tee', 14.99, 'clothing')
cigarettes = main.Products('marlboro', 11.49, 'everything else')
coat = main.Products('coat', 199.99, 'clothing')
coat_return = main.Products('coat', -199.99, 'clothing')


# test to check if sales tax was applied correctly
def test_checkout():
    assert main.checkout(milk, 'MA') == 2.99
    assert main.checkout(tee, 'NH') == 14.99
    assert main.checkout(cigarettes, 'MA') == round(11.49 + (11.49 * 0.0625), 2)
    assert main.checkout(cigarettes, 'ME') == round(11.49 + (11.49 * 0.055), 2)
    assert main.checkout(coat, 'MA') == round(199.99 + (199.99 * 0.0625), 2)
    assert main.checkout(coat, 'ME') == round(199.99 + (199.99 * 0.055), 2)


# test scenarios where state is written in lower case or invalid state
def test_states():
    assert main.checkout(cigarettes, 'ma') > 0
    assert type(main.checkout(cigarettes, 'boo')) == str  # should return an error string


def test_refunds():
    assert type(main.checkout(coat_return, 'MA')) == str
