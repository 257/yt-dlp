from ..networking import HEADRequest
from urllib.parse import urlparse
from .common import InfoExtractor
from box import Box, BoxList


class URN3IE(InfoExtractor):
    IE_DESC = 'Harvard Library, Digital Collections'
    _VALID_URL = r'https?://nrs.harvard.edu/urn-3:FHCL:[0-9]+'
    _TESTS = [{
        'url': 'https://nrs.harvard.edu/urn-3:FHCL:2453393',
        'info_dict': {
            '_type': 'playlist',
            'categories': ['Constitutionalism',
                           'Coup d’état of February 1921',
                           'Eskandari, Soleiman (Mohsen) Mirza',
                           'Firouz, Firouz (Nosrat al-Dowleh)',
                           'Great Britain',
                           'Iraq',
                           'Pahlavi, Reza Shah (prior to Accession to the Throne)',
                           'Sanjabi Tribe',
                           'Soviet Union',
                           'Tabatabaie, Ziaeddin (Seyyed)',
                           'Tribes',
                           'Vossough, Hassan (Vossough al-Dowleh)',
                           'Iskandarī, Sulaymān (Muḥsin) Mīrzā',
                           'Fīrūz, Fīrūz (Nuṣrat al-Dawlah)',
                           'Īrāq',
                           'Pahlavī, Riz̤ā Shāh (prior to Accession to the Throne)',
                           'Sanjābī Tribe',
                           'Ṭabāṭabāʾī, Z̤iyā al-Dīn (Sayyid)',
                           'Vus̱ūq, Ḥasan (Vus̱ūq al-Dawlah)'],
            'channel': 'iohp',
            'channel_id': '15',
            'channel_title': 'Iranian Oral History Project',
            'channel_url': 'https://id.lib.harvard.edu/curiosity/iranian-oral-history-project/32-',
            'description': ['Interviewee: Sanjabi, Karim',
                            'Interviewer: Zia Sedghi',
                            'biographical/historical: Son of Ghassem Khan Sardar- Nasser '
                            '(landowner). University education in law in Paris, civil '
                            'servant. Professor, Tehran University, Vice dean of Faculty '
                            'of Law (1943-44), dean of Faculty of Law (1943-44), minister '
                            'of education (1951), 17th Majles deputy from Kermanshah, '
                            'leader of the National Front, and minister of foreign '
                            'affairs (1979). [Shimoni, p. 205.]',
                            'gender: Male',
                            'tape number: 01'],
            'entries': [{'age_limit': None,
                         'alt_title': None,
                         'channel': 'iohp',
                         'channel_id': '15',
                         'description': ['Interviewee: Sanjabi, Karim',
                                         'Interviewer: Zia Sedghi',
                                         'biographical/historical: Son of Ghassem Khan Sardar- Nasser '
                                         '(landowner). University education in law in Paris, civil '
                                         'servant. Professor, Tehran University, Vice dean of Faculty '
                                         'of Law (1943-44), dean of Faculty of Law (1943-44), minister '
                                         'of education (1951), 17th Majles deputy from Kermanshah, '
                                         'leader of the National Front, and minister of foreign '
                                         'affairs (1979). [Shimoni, p. 205.]',
                                         'gender: Male',
                                         'tape number: 01'],
                         'duration': None,
                         'episode_number': None,
                         'formats': [{'ext': 'mp4',
                                      'format_id': '196',
                                      'format_index': None,
                                      'fps': None,
                                      'has_drm': False,
                                      'manifest_url': 'https://mps.lib.harvard.edu/vod/_definst_/smil:s3/drs-delivery-prod/460210620.smil_97C8E0C812A3DDF9482EA9EAE83360C4/playlist.m3u8',
                                      'preference': None,
                                      'protocol': 'm3u8_native',
                                      'quality': None,
                                      'tbr': 196.608,
                                      'url': 'https://mps.lib.harvard.edu/vod/_definst_/smil:s3/drs-delivery-prod/460210620.smil_97C8E0C812A3DDF9482EA9EAE83360C4/chunklist_w1601907355_b196608_pd1920.m3u8'}],
                         'genre': 'Oral histories',
                         'id': '460210620-0',
                         'playlist_id': '460210620',
                         'playlist_index': 0,
                         'playlist_title': 'Interview with Sanjabi, Karim:  Tape 01',
                         'release_year': 20181217,
                         'season_number': None,
                         'subtitles': {},
                         'thumbnail': None,
                         'timestamp': None,
                         'title': 'Interview with Sanjabi, Karim:  Tape 01'},
                        {'age_limit': None,
                         'alt_title': None,
                         'channel': 'iohp',
                         'channel_id': '15',
                         'description': ['Interviewee: Sanjabi, Karim',
                                         'Interviewer: Zia Sedghi',
                                         'biographical/historical: Son of Ghassem Khan Sardar- Nasser '
                                         '(landowner). University education in law in Paris, civil '
                                         'servant. Professor, Tehran University, Vice dean of Faculty '
                                         'of Law (1943-44), dean of Faculty of Law (1943-44), minister '
                                         'of education (1951), 17th Majles deputy from Kermanshah, '
                                         'leader of the National Front, and minister of foreign '
                                         'affairs (1979). [Shimoni, p. 205.]',
                                         'gender: Male',
                                         'tape number: 01'],
                         'duration': None,
                         'episode_number': None,
                         'formats': [{'ext': 'mp4',
                                      'format_id': '196',
                                      'format_index': None,
                                      'fps': None,
                                      'has_drm': False,
                                      'manifest_url': 'https://mps.lib.harvard.edu/vod/_definst_/smil:s3/drs-delivery-prod/460210620_1.smil_97C8E0C812A3DDF9482EA9EAE83360C4/playlist.m3u8',
                                      'preference': None,
                                      'protocol': 'm3u8_native',
                                      'quality': None,
                                      'tbr': 196.608,
                                      'url': 'https://mps.lib.harvard.edu/vod/_definst_/smil:s3/drs-delivery-prod/460210620_1.smil_97C8E0C812A3DDF9482EA9EAE83360C4/chunklist_w1775040649_b196608_ps1920_pd1879386.m3u8'}],
                         'genre': 'Oral histories',
                         'id': '460210620-1',
                         'playlist_id': '460210620',
                         'playlist_index': '1',
                         'playlist_title': 'Interview with Sanjabi, Karim:  Tape 01',
                         'release_year': 20181217,
                         'season_number': None,
                         'subtitles': {},
                         'thumbnail': None,
                         'timestamp': None,
                         'title': 'Interview with Sanjabi, Karim:  Tape 01'},
                        {'age_limit': None,
                         'alt_title': None,
                         'channel': 'iohp',
                         'channel_id': '15',
                         'description': ['Interviewee: Sanjabi, Karim',
                                         'Interviewer: Zia Sedghi',
                                         'biographical/historical: Son of Ghassem Khan Sardar- Nasser '
                                         '(landowner). University education in law in Paris, civil '
                                         'servant. Professor, Tehran University, Vice dean of Faculty '
                                         'of Law (1943-44), dean of Faculty of Law (1943-44), minister '
                                         'of education (1951), 17th Majles deputy from Kermanshah, '
                                         'leader of the National Front, and minister of foreign '
                                         'affairs (1979). [Shimoni, p. 205.]',
                                         'gender: Male',
                                         'tape number: 01'],
                         'duration': None,
                         'episode_number': None,
                         'formats': [{'ext': 'mp4',
                                      'format_id': '196',
                                      'format_index': None,
                                      'fps': None,
                                      'has_drm': False,
                                      'manifest_url': 'https://mps.lib.harvard.edu/vod/_definst_/smil:s3/drs-delivery-prod/460210620_2.smil_97C8E0C812A3DDF9482EA9EAE83360C4/playlist.m3u8',
                                      'preference': None,
                                      'protocol': 'm3u8_native',
                                      'quality': None,
                                      'tbr': 196.608,
                                      'url': 'https://mps.lib.harvard.edu/vod/_definst_/smil:s3/drs-delivery-prod/460210620_2.smil_97C8E0C812A3DDF9482EA9EAE83360C4/chunklist_w1237246000_b196608_pd233.m3u8'}],
                         'genre': 'Oral histories',
                         'id': '460210620-2',
                         'playlist_id': '460210620',
                         'playlist_index': '2',
                         'playlist_title': 'Interview with Sanjabi, Karim:  Tape 01',
                         'release_year': 20181217,
                         'season_number': None,
                         'subtitles': {},
                         'thumbnail': None,
                         'timestamp': None,
                         'title': 'Interview with Sanjabi, Karim:  Tape 01'},
                        {'age_limit': None,
                         'alt_title': None,
                         'channel': 'iohp',
                         'channel_id': '15',
                         'description': ['Interviewee: Sanjabi, Karim',
                                         'Interviewer: Zia Sedghi',
                                         'biographical/historical: Son of Ghassem Khan Sardar- Nasser '
                                         '(landowner). University education in law in Paris, civil '
                                         'servant. Professor, Tehran University, Vice dean of Faculty '
                                         'of Law (1943-44), dean of Faculty of Law (1943-44), minister '
                                         'of education (1951), 17th Majles deputy from Kermanshah, '
                                         'leader of the National Front, and minister of foreign '
                                         'affairs (1979). [Shimoni, p. 205.]',
                                         'gender: Male',
                                         'tape number: 01'],
                         'duration': None,
                         'episode_number': None,
                         'formats': [{'ext': 'mp4',
                                      'format_id': '196',
                                      'format_index': None,
                                      'fps': None,
                                      'has_drm': False,
                                      'manifest_url': 'https://mps.lib.harvard.edu/vod/_definst_/smil:s3/drs-delivery-prod/460210620_3.smil_97C8E0C812A3DDF9482EA9EAE83360C4/playlist.m3u8',
                                      'preference': None,
                                      'protocol': 'm3u8_native',
                                      'quality': None,
                                      'tbr': 196.608,
                                      'url': 'https://mps.lib.harvard.edu/vod/_definst_/smil:s3/drs-delivery-prod/460210620_3.smil_97C8E0C812A3DDF9482EA9EAE83360C4/chunklist_w487624460_b196608_ps233_pd1810947.m3u8'}],
                         'genre': 'Oral histories',
                         'id': '460210620-3',
                         'playlist_id': '460210620',
                         'playlist_index': '3',
                         'playlist_title': 'Interview with Sanjabi, Karim:  Tape 01',
                         'release_year': 20181217,
                         'season_number': None,
                         'subtitles': {},
                         'thumbnail': None,
                         'timestamp': None,
                         'title': 'Interview with Sanjabi, Karim:  Tape 01'}],
            'extractor': 'URN3',
            'genre': 'Oral histories',
            'id': '460210620',
            'language': 'Persian',
            'location': 'Chico, CA',
            'objid': '460210618',
            'original_url': 'https://nrs.harvard.edu/urn-3:FHCL:2453393',
            'protocol': 'm3u8_native',
            'release_date': '1983-10-15',
            'series': {'part': 'Tape 01', 'title': 'Interview with Sanjabi, Karim: '},
            'subjects': ['Constitutionalism',
                         'Coup d’état of February 1921',
                         'Eskandari, Soleiman (Mohsen) Mirza',
                         'Firouz, Firouz (Nosrat al-Dowleh)',
                         'Great Britain',
                         'Iraq',
                         'Pahlavi, Reza Shah (prior to Accession to the Throne)',
                         'Sanjabi Tribe',
                         'Soviet Union',
                         'Tabatabaie, Ziaeddin (Seyyed)',
                         'Tribes',
                         'Vossough, Hassan (Vossough al-Dowleh)',
                         'Iskandarī, Sulaymān (Muḥsin) Mīrzā',
                         'Fīrūz, Fīrūz (Nuṣrat al-Dawlah)',
                         'Īrāq',
                         'Pahlavī, Riz̤ā Shāh (prior to Accession to the Throne)',
                         'Sanjābī Tribe',
                         'Ṭabāṭabāʾī, Z̤iyā al-Dīn (Sayyid)',
                         'Vus̱ūq, Ḥasan (Vus̱ūq al-Dawlah)'],
            'title': 'Interview with Sanjabi, Karim:  Tape 01',
            'upload_date': '20181217',
            'url': 'https://mps.lib.harvard.edu/sds/audio/460210620'
        }
    }]
    info = Box(extractor="URN3", description=[], series={})

    def _real_extract(self, url):
        self.info.original_url = self.info.url = url

        harvard = Box(
            self._download_json(
                'https://api.lib.harvard.edu/v2/items.json',
                'Fetching metadata for',
                url,
                query={
                    'urn': url.split('/')[-1]
                },
            )['items']
        )
        from pprint import pformat
        print(pformat(harvard.to_dict()))
        for i in harvard.mods:
            if not hasattr(i, 'name'):
                continue

            for n in i.name:
                if isinstance(n.role, BoxList):
                    for r in n.role:
                        if r.roleTerm in ("Interviewee", "Interviewer"):
                            self.info.description += [f"{r.roleTerm}: {n.namePart}"]
                elif n.role.roleTerm in ("Interviewee", "Interviewer"):
                    self.info.description += [f"{n.role.roleTerm}: {n.namePart}"]

            self.info.description += [f"{n.type}: {n.text}" for n in i.note]

            for e in i.extension:
                if hasattr(e, "sets"):
                    self.info.channel_id = e.sets.set.systemId
                    self.info.channel_url = e.sets.set.baseUrl
                    self.info.channel_title = e.sets.set.setName
                    self.info.channel = e.sets.set.setSpec
                if (hasattr(e, 'DRSMetadata') and e.DRSMetadata.uriType in
                        ("SDS", "SDS_VIDEO")):
                    if e.DRSMetadata.uriType == "SDS":
                        self.info._type = "audio"
                    self.info.id = e.DRSMetadata.drsFileId
                    self.info.objid = e.DRSMetadata.drsObjectId
                    self.info.upload_date = e.DRSMetadata.insertionDate.split('T')[0].replace('-', '')

            self.info.title = i.titleInfo.title
            if hasattr(i.titleInfo, 'partNumber'):
                self.info.series.title = self.info.title
                self.info.series.part = f"{i.titleInfo.partNumber}"
                self.info.title += f" {i.titleInfo.partNumber}"

            self.info.categories = [
                s.topic for s in i.subject if hasattr(s, 'topic')
            ]
            self.info.subjects = self.info.categories

            self.info.location = i.originInfo.place.placeTerm
            self.info.genre = i.genre

            if i.language.languageTerm.type == 'text':
                self.info.language = i.language.languageTerm.text

            self.info.release_date = i.originInfo.dateCaptured

            self._find_entries()

        return self.info

    def _follow_redirect(self) -> None:
        """Follow and Report information extraction."""
        while (urlparse(self.info.url).netloc != "mps.lib.harvard.edu"):
            self.info.url = self._request_webpage(
                HEADRequest(self.info.url),
                video_id=self.info.id,
                note='Resolving final URL',
                errnote='Could not resolve final URL'
            ).url

    def _find_entries(self):
        self._follow_redirect()
        webpage = self._download_webpage(self.info.url, self.info.id)
        jwplayer_extracetd = self._extract_jwplayer_data(
            webpage=webpage,
            video_id=self.info.id,
            require_title=False
        )

        if jwplayer_extracetd is not None:
            self.info._type = jwplayer_extracetd['_type']
            self.info.entries = []
            for e in jwplayer_extracetd.get('entries'):
                idx = e['formats'][0]['manifest_url']\
                        .split('drs-delivery-prod/')[1]\
                        .split('.')[0]\
                        .split('_')
                e.update({
                    'playlist_index': 0 if idx[-1] == e['id'] else idx[-1]
                })
                e.update({
                    'id': f"{e['id']}-{e['playlist_index']}",
                    'title': self.info.title,
                    'playlist_title': self.info.title,
                    'playlist_id': e['id'],
                    'channel': self.info.channel,
                    'channel_id': self.info.channel_id,
                    'description': self.info.description,
                    'genre': self.info.genre,
                    'release_year': int(self.info.upload_date),
                })
                self.info.entries += [e]
                self.info.protocol = e['formats'][0]['protocol']
