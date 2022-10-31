from base_object.errors import AssertionErrors


class Helper:
    def generation_list(self, sort_object):
        self.list1 = []
        for x in sort_object:
            price = x.text
            self.list1.append(price)
        return self.list1

    def equal(self, expected, actual):
        assert expected == actual, AssertionErrors.EQUALERROR.format(expected, actual)
