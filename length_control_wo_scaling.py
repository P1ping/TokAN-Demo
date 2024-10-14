from dominate.tags import *


systems = [
    ("Source", "source", "{spk}_{sid}.wav"),
    ("Proposed w/ 0.5x dur.", "dur_x0.5", "{spk}_{sid}.gen.wav"),
    ("Proposed w/ 1.0x dur.", "dur_x1.0", "{spk}_{sid}.gen.wav"),
    ("Proposed w/ 1.5x dur.", "dur_x1.5", "{spk}_{sid}.gen.wav"),
]

samples = [
    (
        "BWC",
        "arctic_b0095",
        "He heard a sound which brought him quickly into consciousness of day.",
    ),
    (
        "LXC",
        "arctic_b0383",
        "A bush chief had died a natural death.",
    ),
    (
        "NCC",
        "arctic_b0419",
        "Your father's fifth command, he nodded.",
    ),
    (
        "TXHC",
        "arctic_a0053",
        "Suddenly his fingers closed tightly over the handkerchief.",
    ),
    (
        "BWC",
        "arctic_a0103",
        "But there came no promise from the bow of the canoe.",
    ),
    (
        "LXC",
        "arctic_b0450",
        "To my dearest and always appreciated friend, I submit myself.",
    ),
    (
        "NCC",
        "arctic_a0209",
        "It was not a large lake, and almost round.",
    ),
    (
        "TXHC",
        "arctic_b0441",
        "And there was Ethel Baird, whom also you must remember.",
    ),
    (
        "BWC",
        "arctic_a0463",
        "They are his tongue, by which he makes his knowledge articulate.",
    ),
    (
        "LXC",
        "arctic_a0045",
        "He moved away as quietly as he had come.",
    ),
    (
        "NCC",
        "arctic_a0589",
        "I was sick once -- typhoid.",
    ),
    (
        "TXHC",
        "arctic_a0103",
        "But there came no promise from the bow of the canoe.",
    ),
    (
        "BWC",
        "arctic_a0367",
        "There is not an iota of truth in it, certainly not.",
    ),
    (
        "LXC",
        "arctic_b0383",
        "A bush chief had died a natural death.",
    ),
    (
        "NCC",
        "arctic_b0344",
        "Lots of men take women buggy riding.",
    ),
    (
        "TXHC",
        "arctic_a0109",
        "Do you know that you are shaking my confidence in you.",
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
                for spk, _, _ in samples:
                    th(spk, scope="col")
        with tbody():
            with tr():
                th(
                    "Text",
                    scope="row",
                    style="position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                )
                for _, _, text in samples:
                    td(p(text))

            for sys_name, sys_id, fname_pattern in systems:
                with tr():
                    th(
                        sys_name,
                        scope="row",
                        style="white-space: nowrap; position: sticky; left: 0; z-index:10; opacity: 1.0; background-color: white;",
                    )
                    for spk, key, _ in samples:
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
