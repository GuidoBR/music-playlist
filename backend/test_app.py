import unittest
import json
import app

from unittest.mock import MagicMock, patch

class TestApp(unittest.TestCase):

    def test_get_random_word_returns_word_from_list(self):
        self.assertIn(app.get_random_word('String with words'), ['String', 'with', 'words'])

    @patch('app.get_lyrics')
    @patch('app.get_tracks')
    def test_get_music_information_returns_expected_information(self, mock_tracks, mock_lyrics):
        mock_tracks.return_value = [{
                    "track": {
                        "track_id": 118228732,
                        "track_name": "Mister Sandman (In the Style of the Four Aces) [Karaoke Version]",
                        "album_name": "Thank God Its Friday (TGIF)",
                        "artist_id": 32446372,
                        "artist_name": "Jamie C feat. Hollywood Luck",
                        "track_share_url": "https:\/\/www.musixmatch.com\/lyrics\/Jamie-C-feat-Hollywood-Luck\/Thank-God-Its-Friday-TGIF?utm_source=application&utm_campaign=api&utm_medium=Draper+AI%3A1409619881554"
                    }
                },
                {
                    "track": {
                        "track_id": 118353823,
                        "track_name": "Moonlight",
                        "album_name": "Dawn of Time",
                        "artist_id": 26643138,
                        "artist_name": "Shaun Allaway",
                        "track_share_url": "https:\/\/www.musixmatch.com\/lyrics\/Shaun-Allaway\/Moonlight?utm_source=application&utm_campaign=api&utm_medium=Draper+AI%3A1409619881554"
                    }
                }
            ]
        mock_lyrics.return_value = "Mr. Sandman Mr. Sandman Mr. Sandman, bring me a dream Make her complexion like pictures in green Give her two lips like roses and clover Then tell me that my lonesome nights are over Sandman, I'm so alone Don't have nobody to call my own Please turn on your magic beam Mr. Sandman, bring me a dream Mr. Sandman, bring me a dream ... ******* This Lyrics is NOT for Commercial use ******* (1409619881554)"
        
        music = app.get_music_information('Sandman')
        self.assertEqual(music.get('lyrics'), mock_lyrics.return_value)
        self.assertEqual(music.get('track_name'), mock_tracks.return_value[0].get("track").get("track_name"))
        self.assertEqual(music.get('artist_name'), mock_tracks.return_value[0].get("track").get("artist_name"))
        self.assertEqual(music.get('url'), mock_tracks.return_value[0].get("track").get("track_share_url"))

if __name__ == '__main__':
    unittest.main()