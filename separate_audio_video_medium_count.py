PLUGIN_NAME = u"Separate audio and video medium count"
PLUGIN_AUTHOR = u"Mark Trolley"
PLUGIN_DESCRIPTION = u'''Separates the count of audio mediums and video mediums
for a release. With this plugin you can use %_totalaudiomediums% and/or
%_totalvideomediums% instead of %totaldiscs% in file name formatting.'''
PLUGIN_VERSION = "0.2"
PLUGIN_API_VERSIONS = [ "2.0" ]

from picard.metadata import register_album_metadata_processor

video_mediums = [ u"DVD", u"DVD-Video", u"Blu-ray", u"HD-DVD", u"Videotape",
                  u"VHS", u"Betamax", u"VCD", u"CDV", u"SVCD", u"LaserDisc" ]

def count_release_mediums(tagger, metadata, release):
    total_video_mediums = 0
    total_mediums = int(metadata["totaldiscs"] or "0")
    if total_mediums > 1:
        for medium in release["media"]:
            if (medium["format"] in video_mediums):
                total_video_mediums += 1
    metadata["~totalvideomediums"] = total_video_mediums
    metadata["~totalaudiomediums"] = total_mediums - total_video_mediums

register_album_metadata_processor(count_release_mediums)
