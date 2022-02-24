from ..models import Result, Membership, Course, Resource
from django.contrib.auth.models import User


def has_staff_membership_to_organisation(user: User, organisation_id: str) -> Result:
    return _has_membership_to_organisation(user, organisation_id, "STAFF")


def has_staff_membership_to_course(user: User, course_id: str) -> Result:
    return _has_membership_to_course(user, course_id, "STAFF")


def has_staff_membership_to_resource(user: User, resource_id: str) -> Result:
    return _has_membership_to_resource(user, resource_id, "STAFF")


def has_student_membership_to_course(user: User, course_id: str) -> Result:
    return _has_membership_to_course(user, course_id, "STUDENT")


def has_student_membership_to_resource(user: User, resource_id: str) -> Result:
    return _has_membership_to_resource(user, resource_id, "STUDENT")


def _has_membership_to_organisation(user: User, organisation_id: str, role: str) -> Result:
    if user.is_anonymous:
        return Result(error="Not logged in")

    memberships = Membership.objects.filter(
        organisation_id=organisation_id,
        user=user.id,
        role=role)
    return Result(data=len(memberships) > 0)


def _has_membership_to_course(user: User, course_id: str, role: str) -> Result:
    if user.is_anonymous:
        return Result(error="Not logged in")

    course = Course.objects.filter(id=course_id).first()
    if course is None:
        return Result(error="Course " + course_id + " not found")

    memberships = Membership.objects.filter(
        organisation_id=course.organisation.id,
        course_id=course.id,
        user=user.id,
        role=role)
    return Result(data=len(memberships) > 0)


def _has_membership_to_resource(user: User, resource_id: str, role: str) -> Result:
    if user.is_anonymous:
        return Result(error="Not logged in")

    resource = Resource.objects.filter(id=resource_id).first()
    if resource is None:
        return Result(error="Resource " + resource_id + " not found")

    memberships = Membership.objects.filter(
        organisation_id=resource.course.organisation.id,
        course_id=resource.course.id,
        user=user.id,
        role=role)
    return Result(data=len(memberships) > 0)
