class Television:
    MIN_CHANNEL = 0     # Minimum TV channel
    MAX_CHANNEL = 3     # Maximum TV channel

    MIN_VOLUME = 0      # Minimum TV volume
    MAX_VOLUME = 2      # Maximum TV volume

    def __init__(self) -> None:
        """
        Constructor to set up Television class
        """
        self.__channel = Television.MIN_CHANNEL
        self.__volume = Television.MIN_VOLUME
        self.__is_turned_on = False

    def power(self) -> None:
        """
        Sets TV power on or off
        """
        if self.__is_turned_on:
            self.__is_turned_on = False
        else:
            self.__is_turned_on = True

    def channel_up(self) -> None:
        """
        Turns channel up by 1. If the channel equals 3 the channel is set to 0
        """
        if self.__channel == Television.MAX_CHANNEL and self.__is_turned_on:
            self.__channel = Television.MIN_CHANNEL
        elif self.__channel < Television.MAX_CHANNEL and self.__is_turned_on:
            self.__channel += 1

    def channel_down(self) -> None:
        """
        Turns channel down by 1. If the channel equals 0 the channel is set to 3
        """
        if self.__channel == Television.MIN_CHANNEL and self.__is_turned_on:
            self.__channel = Television.MAX_CHANNEL
        elif self.__channel > Television.MIN_CHANNEL and self.__is_turned_on:
            self.__channel -= 1

    def volume_up(self) -> None:
        """
        Turns volume up by 1. If the volume equals 2 the volume is set to 0
        """
        if self.__volume < Television.MAX_VOLUME and self.__is_turned_on:
            self.__volume += 1

    def volume_down(self) -> None:
        """
        Turns volume down by 1. If the volume equals 0 the volume is set to 2
        """
        if self.__volume > Television.MIN_VOLUME and self.__is_turned_on:
            self.__volume -= 1

    def __str__(self) -> str:
        """
        method to get TV status
        :return: status of the TV(power, channel #, and volume)
        """

        return f"TV status: Is on = {self.__is_turned_on}, Channel = {self.__channel}, Volume = {self.__volume}"
