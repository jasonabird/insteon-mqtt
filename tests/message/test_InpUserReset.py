#===========================================================================
#
# Tests for: insteont_mqtt/message/InpUserReset.py
#
#===========================================================================
import insteon_mqtt.message as Msg


class Test_InpUserReset:
    #-----------------------------------------------------------------------
    def test_in(self):
        b = bytes([0x02, 0x55])
        obj = Msg.InpUserReset.from_bytes(b)

        str(obj)

    #-----------------------------------------------------------------------


#===========================================================================
