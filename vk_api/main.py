from secret import LOGIN, PASSWORD
from vk_api import VkUpload, VkApi


def main():
    vk_sess = VkApi(login=LOGIN, password=PASSWORD)
    vk_sess.auth()
    vk = vk_sess.get_api()

    upload = VkUpload(vk)
    upload.photo(['static/python.jpg'], album_id=23456789, group_id=34567890)


if __name__ == '__main__':
    main()
