import trial;

def test_return_required_output():
    assert trial.hello() == "Hello world"

def test_sum_of_corresponding():
    assert trial.sum_of_corresponding([1,2],[2,3]) == [3,5]