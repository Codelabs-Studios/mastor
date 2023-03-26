import discord


class Perm:
    @staticmethod
    def administator():
        return discord.Permissions(8)

    @staticmethod
    def view_audit_log():
        return discord.Permissions(128)

    @staticmethod
    def manage_guild():
        return discord.Permissions(32)

    @staticmethod
    def manage_roles():
        return discord.Permissions(268435456)

    @staticmethod
    def manage_channels():
        return discord.Permissions(16)

    @staticmethod
    def kick_members():
        return discord.Permissions(2)

    @staticmethod
    def ban_members():
        return discord.Permissions(4)

    @staticmethod
    def create_instant_invite():
        return discord.Permissions(1)

    @staticmethod
    def change_nickname():
        return discord.Permissions(67108864)

    @staticmethod
    def manage_nicknames():
        return discord.Permissions(134217728)

    @staticmethod
    def manage_emojis_and_stickers():
        return discord.Permissions(1073741824)

    @staticmethod
    def manage_webhooks():
        return discord.Permissions(536870912)

    @staticmethod
    def view_channel():
        return discord.Permissions(1024)

    @staticmethod
    def manage_events():
        return discord.Permissions(8589934592)

    @staticmethod
    def moderate_members():
        return discord.Permissions(1099511627776)

    @staticmethod
    def view_server_insights():
        return discord.Permissions(524288)

    @staticmethod
    def view_creator_monetization_insights():
        return discord.Permissions(2199023255552)

    @staticmethod
    def send_messages():
        return discord.Permissions(2048)

    @staticmethod
    def create_public_threads():
        return discord.Permissions(34359738368)

    @staticmethod
    def create_private_threads():
        return discord.Permissions(68719476736)

    @staticmethod
    def send_messages_in_threads():
        return discord.Permissions(274877906944)

    @staticmethod
    def send_tts_messages():
        return discord.Permissions(4096)

    @staticmethod
    def manage_messages():
        return discord.Permissions(8192)

    @staticmethod
    def manage_threads():
        return discord.Permissions(17179869184)

    @staticmethod
    def embed_links():
        return discord.Permissions(16384)

    @staticmethod
    def attach_files():
        return discord.Permissions(32768)

    @staticmethod
    def read_message_history():
        return discord.Permissions(65536)

    @staticmethod
    def mention_everyone():
        return discord.Permissions(131072)

    @staticmethod
    def use_external_emojis():
        return discord.Permissions(262144)

    @staticmethod
    def use_external_stickers():
        return discord.Permissions(137438953472)

    @staticmethod
    def add_reactions():
        return discord.Permissions(64)

    @staticmethod
    def use_slash_commands():
        return discord.Permissions(2147483648)

    @staticmethod
    def connect():
        return discord.Permissions(1048576)

    @staticmethod
    def speak():
        return discord.Permissions(2097152)

    @staticmethod
    def video():
        return discord.Permissions(512)

    @staticmethod
    def mute_members():
        return discord.Permissions(4194304)

    @staticmethod
    def deafen_members():
        return discord.Permissions(8388608)

    @staticmethod
    def move_members():
        return discord.Permissions(16777216)

    @staticmethod
    def use_voice_activity():
        return discord.Permissions(33554432)

    @staticmethod
    def priority_speaker():
        return discord.Permissions(256)

    @staticmethod
    def request_to_speak():
        return discord.Permissions(4294967296)

    @staticmethod
    def use_embedded_activities():
        return discord.Permissions(549755813888)

    @staticmethod
    def use_soundboard():
        return discord.Permissions(4398046511104)
