%global pkg_name maven-invoker
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.1.1
Release:        9.10%{?dist}
Summary:        Fires a maven build in a clean environment
License:        ASL 2.0
URL:            http://maven.apache.org/shared/maven-invoker/
Source0:        http://repo1.maven.org/maven2/org/apache/maven/shared/%{pkg_name}/%{version}/%{pkg_name}-%{version}-source-release.zip
Patch0:         %{pkg_name}-MSHARED-278.patch
Patch1:         %{pkg_name}-MSHARED-279.patch

BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}javapackages-tools
BuildRequires:  %{?scl_prefix_java_common}junit
BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  maven30-maven-surefire-provider-junit
BuildRequires:  maven30-maven-shared


%description
This API is concerned with firing a Maven build in a new JVM. It accomplishes
its task by building up a conventional Maven command line from options given in
the current request, along with those global options specified in the invoker
itself. Once it has the command line, the invoker will execute it, and capture
the resulting exit code or any exception thrown to signal a failure to execute.
Input/output control can be specified using an InputStream and up to two
InvocationOutputHandlers.

This is a replacement package for maven-shared-invoker

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.


%prep
%setup -q -n %{pkg_name}-%{version}
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%patch0 -p1
%patch1 -p1

%mvn_file : %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_build -f
%{?scl:EOF}

%install
%{?scl:scl enable maven30 %{scl} - <<"EOF"}
set -e -x
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE NOTICE

%files javadoc -f .mfiles-javadoc
%doc LICENSE NOTICE


%changelog
* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 2.1.1-9.10
- maven33 rebuild

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.1.1-9.9
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.1.1-9.8
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-9.7
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-9.6
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-9.5
- Mass rebuild 2014-02-18

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-9.4
- Remove requires on java

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-9.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-9.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-9.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.1.1-9
- Mass rebuild 2013-12-27

* Mon Aug 26 2013 Michal Srb <msrb@redhat.com> - 2.1.1-8
- Migrate away from mvn-rpmbuild (Resolves: #997507)

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-7
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Wed Mar 13 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.1.1-6
- Add patch for MSHARED-278, resolves rhbz#921068
- Add patch for MSHARED-279, resolves rhbz#921067

* Wed Feb 20 2013 Tomas Radej <tradej@redhat.com> - 2.1.1-5
- Added B/R on maven-shared

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.1.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.1.1-3
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Mon Jan 14 2013 Tomas Radej <tradej@redhat.com> - 2.1.1-2
- Disabled tests

* Fri Jan 11 2013 Tomas Radej <tradej@redhat.com> - 2.1.1-1
- Initial version

