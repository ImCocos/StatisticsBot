"""
Message parsers
"""
from aiogram import types

# from logger import get_logger


# logger = get_logger(__name__)


class MatParser:
    """Mat parser

    Returns:
        MatParser: parser
    """
    mats_list = [
        'хуй',
        'бля',
        'пизд',
        'хер',
        'сука',
        'сучка',
    ]

    @classmethod
    def _count_mat(cls, text: str, mat: str) -> int:
        res = 0
        start = 0
        l = len(mat)

        while True:
            mat_idx = text.find(mat, start)
            if mat_idx != -1:
                start = mat_idx + l
                if start == mat_idx:
                    break
                res += 1
            else:
                return res
        return 0

    @classmethod
    def _count_mats(cls, text: str) -> dict:
        res = {}
        for mat in cls.mats_list:
            res[mat] = cls._count_mat(text, mat)

        return res


    @classmethod
    def _parse_text(cls, text: str) -> None:
        mats = cls._count_mats(text)

    @classmethod
    def parse_msg(cls, message: types.Message) -> None:
        """Parse message on content type

        Args:
            message (types.Message): msg
        """
        content_type: str = message.content_type
        logger.info('Parsing msg')

        match content_type:
            case types.ContentType.TEXT:
                logger.info('Parsing msg like text')
                cls._parse_text(message.text) # type: ignore

p = MatParser()

print(p._count_mats('Очень блять матный нахуй текст, пиздец просто блять'))
