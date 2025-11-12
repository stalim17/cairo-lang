load("//src/starkware/cairo/lang:cairo_rules.bzl", "cairo_library")

cairo_library(
    name = "starknet_common_cairo_lib",
    srcs = [
        "constants.cairo",
        "eth_utils.cairo",
        "messages.cairo",
        "storage.cairo",
        "syscalls.cairo",
    ],
    visibility = ["//visibility:public"],
    deps = [
        "//src/starkware/cairo/common:cairo_common_cairo_lib",
    ],
)

package(default_visibility = ["//visibility:public"])

exports_files([
    "constants.cairo",
    "storage.cairo",
    "syscalls.cairo",
])
