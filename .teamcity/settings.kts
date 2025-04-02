import jetbrains.buildServer.configs.kotlin.*
import jetbrains.buildServer.configs.kotlin.buildFeatures.perfmon
import jetbrains.buildServer.configs.kotlin.buildSteps.script
import jetbrains.buildServer.configs.kotlin.triggers.vcs

version = "2024.12"

project {
    buildType(Build)
    buildType(SnapshotDependentJob)
    buildType(ParallelJob)
}

object Build : BuildType({
    name = "Build"

    vcs {
        root(DslContext.settingsRoot)
    }

    steps {
        script {
            id = "simpleRunner"
            scriptContent = """echo "mama!""""
        }
    }

    triggers {
        vcs {
        }
    }

    features {
        perfmon {
        }
    }
})

object SnapshotDependentJob : BuildType({

    name = "Snapshot Dependent Job"

    dependencies {
        snapshot(Build) {}
        snapshot(ParallelJob) {}
    }

    steps {
        script {
            id = "dependentRunner"
            scriptContent = """echo "papa!""""
        }
    }
})

object ParallelJob : BuildType({
    name = "Parallel Job"

    steps {
        script {
            id = "parallelRunner"
            scriptContent = """echo "brother!""""
        }
    }
})
