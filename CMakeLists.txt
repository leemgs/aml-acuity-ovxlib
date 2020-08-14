# Copyright (c) 2018 Samsung Electronics Co., Ltd All Rights Reserved
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
CMAKE_MINIMUM_REQUIRED(VERSION 2.8)

PROJECT("ovxlib")

IF(NOT DEFINED FULLVER)
	SET(FULLVER "5.5.0")
ENDIF(NOT DEFINED FULLVER)

SET(PREFIX ${CMAKE_INSTALL_PREFIX})

IF(NOT DEFINED BINDIR)
	SET(BINDIR "${PREFIX}/bin")
ENDIF(NOT DEFINED BINDIR)

IF(NOT DEFINED LIBDIR)
	SET(LIBDIR "${PREFIX}/lib")
ENDIF(NOT DEFINED LIBDIR)

IF(NOT DEFINED PCDIR)
	SET(PCDIR "${PREFIX}/lib/pkgconfig")
ENDIF(NOT DEFINED PCDIR)

IF(NOT DEFINED INCDIR)
	SET(INCDIR "${PREFIX}/include/${PROJECT_NAME}")
ENDIF(NOT DEFINED INCDIR)

SET(dependents "aml-npu-sdk")
SET(pc_dependents "aml-npu-sdk")

SET(PC_NAME ${PROJECT_NAME})
SET(PC_REQUIRED ${pc_dependents})
SET(PC_LDFLAGS -l${PROJECT_NAME})
SET(PC_DESCRIPTION "Acuity OVX Library")
CONFIGURE_FILE(
    ${PROJECT_NAME}.pc.in
    ${PROJECT_NAME}.pc
    @ONLY
)

IF("${ARCH}" STREQUAL "arm")
INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/lib32/libovxlib.so DESTINATION ${LIBDIR})
ELSE("${ARCH}" STREQUAL "arm")
INSTALL(FILES ${CMAKE_CURRENT_SOURCE_DIR}/lib64/libovxlib.so DESTINATION ${LIBDIR})
ENDIF("${ARCH}" STREQUAL "arm")
INSTALL(FILES ${CMAKE_CURRENT_BINARY_DIR}/${PROJECT_NAME}.pc DESTINATION ${PCDIR})
INSTALL(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/ DESTINATION ${INCDIR} FILES_MATCHING PATTERN "*.h")
INSTALL(DIRECTORY ${CMAKE_CURRENT_SOURCE_DIR}/include/ DESTINATION ${INCDIR} FILES_MATCHING PATTERN "*.def")
