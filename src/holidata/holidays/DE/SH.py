from holidata.holidays.holidays import Region


class SH(Region):
    def __init__(self, country):
        super().__init__("SH", country)

        self.define_holiday() \
            .with_name("Reformationstag") \
            .since(2018) \
            .on("10-31") \
            .with_flags("RF")
