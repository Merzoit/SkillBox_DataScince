import vk_api as va

session = va.VkApi(login="", password="")
session.auth()
cookie = session.get_api()
cookie
