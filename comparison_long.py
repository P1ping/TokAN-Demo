from dominate.tags import *

systems = [
    ("Source", "source", "{spk}_{sid}.wav"),
    ("Baseline", "baseline", "{spk}_{sid}.wav"),
    ("Ours", "ours", "{spk}_{sid}.wav"),
    ("Ours w/ dur. scaling", "ours_scaling", "{spk}_{sid}.wav"),
    ("Ours w/ dur. control", "ours_control", "{spk}_{sid}.wav"),
]

samples = [
    (
        "BWC",
        "Chinese",
        "arctic_a0154",
        "He was smooth-shaven, and his hair and eyes were black.",
    ),
    ("BWC", "Chinese", "arctic_a0290", "One by one the boys were captured."),
    ("LXC", "Chinese", "arctic_a0589", "I was sick once -- typhoid."),
    ("LXC", "Chinese", "arctic_a0059", "His immaculate appearance was gone."),
    (
        "YBAA",
        "Arabic",
        "arctic_b0087",
        "They will search for us between their camp and Churchill.",
    ),
    (
        "YDCK",
        "Korean",
        "arctic_b0145",
        "Besides, had he not whipped the big owl in the forest.",
    ),
    ("ERMS", "Spanish", "arctic_b0037", "Philip knew that she was not an Indian."),
    (
        "ERMS",
        "Spanish",
        "arctic_b0048",
        "He looked like one who had passed through an uncomfortable hour or two.",
    ),
    (
        "MBMPS",
        "Spanish",
        "arctic_a0088",
        "He made sure that the magazine was loaded, and resumed his paddling.",
    ),
    (
        "MBMPS",
        "Spanish",
        "arctic_b0145",
        "Besides, had he not whipped the big owl in the forest.",
    ),
    (
        "PNV",
        "Vietnamese",
        "arctic_b0441",
        "And there was Ethel Baird, whom also you must remember.",
    ),
    (
        "PNV",
        "Vietnamese",
        "arctic_b0238",
        "The very thought of the effort to swim over was nauseating.",
    ),
]


def get_table(
    root: str = "./samples",
    control_width_px=240,
) -> html_tag:
    _div = div(cls="table-responsive", style="overflow-x: scroll").add(
        table(cls="table table-sm")
    )
    with _div:
        with thead():
            with tr():
                th("Speaker", scope="col")
                for spk, act, _, _ in samples:
                    th(f"{spk} ({act})", scope="col")
        with tbody():
            with tr():
                th(
                    "Text",
                    scope="row",
                    style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                )
                for _, _, _, text in samples:
                    td(p(text))

            for sys_name, sys_id, fname_pattern in systems:
                with tr():
                    th(
                        sys_name,
                        scope="row",
                        style="white-space: nowrap; position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for spk, _, key, _ in samples:
                        fname = fname_pattern.format(spk=spk, sid=key)
                        td(
                            audio(
                                source(
                                    src=f"{root}/{sys_id}/{fname}",
                                    type="audio/wav",
                                ),
                                controls="",
                                style=f"width: {control_width_px:d}px",
                                preload="none",
                            )
                        )
    return _div
