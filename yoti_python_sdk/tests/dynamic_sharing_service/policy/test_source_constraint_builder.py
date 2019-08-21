from yoti_python_sdk.dynamic_sharing_service.policy.source_constraint_builder import (
    SourceConstraintBuilder,
)
from yoti_python_sdk.dynamic_sharing_service.policy.wanted_anchor_builder import (
    DRIVING_LICENCE,
    PASSPORT,
)


def test_build():
    constraint = SourceConstraintBuilder().build()

    assert constraint["type"] == "SOURCE"
    assert not constraint["preferred_sources"]["soft_preference"]
    assert constraint["preferred_sources"]["anchors"] == []


def test_with_driving_licence():
    constraint = SourceConstraintBuilder().with_driving_licence().build()

    anchors = constraint["preferred_sources"]["anchors"]
    assert len(anchors) == 1
    assert DRIVING_LICENCE in [a["name"] for a in anchors]


def test_with_soft_preference():
    constraint = (
        SourceConstraintBuilder()
        .with_passport()
        .with_driving_licence()
        .with_soft_preference()
        .build()
    )
    anchors = constraint["preferred_sources"]["anchors"]
    assert len(anchors) == 2
    assert DRIVING_LICENCE in [a["name"] for a in anchors]
    assert PASSPORT in [a["name"] for a in anchors]
    assert constraint["preferred_sources"]["soft_preference"]
