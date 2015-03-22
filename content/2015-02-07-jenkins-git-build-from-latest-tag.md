Title: Build a Jenkins Job from Latest Git Tag
Date: 2015-02-07 18:46:37
Modified: 2015-02-07 18:46:37
Category: Tools
Tags: Jenkins, Git
Slug: jenkins-git-build-from-latest-tag
Authors: Ramz
Summary: Build a Jenkins Job from Latest Git Tag

To build a jenkins job from the latest git tag of a repository. Let the tag is of format "release/xxx"

1. Select the Advanced button for git and specify a Refspec in the Jenkin's git plugin
that only selects these tags:

        +refs/tags/release/*:refs/remotes/origin/tags/release/*

2. In the **branch specifier** specify

        */tags/release/*

3. Specify a poll interval so that it polls every x minute. Once you create a tag, jenkins will checkout the code and build it for you.


![JENKINS]({filename}/images/jenkins_build_from_git_tag.png)
