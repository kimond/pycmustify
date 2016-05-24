from cmustify import Cmustify
from nose.tools import assert_equal
from nose.tools import assert_true
from nose.tools import assert_false
from nose.tools import assert_is_not_none
from nose.tools import assert_is_none


class TestCmustify(object):

    def test_init(self):
        cmustify = Cmustify("")
        assert_is_not_none(cmustify.status_data)

    def test_cmus_info_constant(self):
        assert_equal(type(Cmustify.cmus_info), dict)

    def test_parse_data(self):
        cmustify = Cmustify()
        cmustify.parse_data("status playing title Dance with me")
        assert_equal(cmustify.data['status'], "playing")
        assert_equal(cmustify.data['title'], "Dance with me")

    def test_parse_data_from_init(self):
        cmustify = Cmustify("status playing title Dance with me")
        assert_equal(cmustify.data['title'], "Dance with me")

    def test_get_status_data(self):
        cmustify = Cmustify("status playing title hola")
        assert_equal(cmustify.get_data("title"), "hola")

    def test_get_empty_data_return_none(self):
        cmustify = Cmustify("status playing title hola")
        assert_is_none(cmustify.get_data("album"))

    def test_format_notification_body(self):
        cmustify = Cmustify(
                "status playing title Dance with me artist ACBD album dancer")
        assert_equal(cmustify.format_notification_body(),
                     "Dance with me by ACBD, dancer")

    def test_display_song(self):
        cmustify = Cmustify("status playing title Dance with me")
        assert_true(cmustify.display_song())

    def test_display_song_with_status_stopped(self):
        cmustify = Cmustify("status stopped title Dance with me")
        assert_false(cmustify.display_song())
